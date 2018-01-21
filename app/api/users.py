from app.postgres import users
import json, uuid


def create(name, surname, form, schoolcard=None, vk_id=None, tg_id=None):
    if vk_id != None:
        if users.find_by_vk_id(vk_id):
            return json.dumps({'success': False, 'description': 'User already exist.'})
    if tg_id != None:
        if users.find_by_tg_id(tg_id):
            return json.dumps({'success': False, 'description': 'User already exist.'})
    if schoolcard != None:
        if users.find_by_schoolcard(schoolcard):
            return json.dumps({'success': False, 'description': 'User already exist.'})
    approved = True  # Нужна база карт
    """
    Здесь нужно осуществлять проверку валидности карты. Сейчас валидируем всех подряд
    """
    id = str(uuid.uuid4())
    if users.create(id, name, surname, schoolcard, approved, form, vk_id, tg_id):
        user = users.find_by_id(id)
        return json.dumps(
            {'success': True,
             'user': {'id': user[0], 'name': user[1], 'surname': user[2],
                      'schoolcard': user[3], 'approved': user[4],
                      'form': user[5], 'vk_id': user[6], 'tg_id': user[7], 'access': user[8]}})


def check_vk_id(vk_id):
    if users.find_by_vk_id(vk_id):
        return json.dumps({'exist': True})
    else:
        return json.dumps({'exist': False})


def check_tg_id(tg_id):
    if users.find_by_tg_id(tg_id):
        return json.dumps({'exist': True})
    else:
        return json.dumps({'exist': False})


def check_schoolcard(schoolcard):
    if users.find_by_schoolcard(schoolcard):
        return json.dumps({'exist': True})
    else:
        return json.dumps({'exist': False})


def update_account(id, name, surname, schoolcard, approved, form, vk_id, tg_id, access):
    if users.find_by_id(id):
        if users.update(id, name, surname, schoolcard, approved, form, vk_id, tg_id, access):
            user = users.find_by_id(id)
            return json.dumps(
                {'success': True,
                 'user': {'id': user[0], 'name': user[1], 'surname': user[2],
                          'schoolcard': user[3], 'approved': user[4],
                          'form': user[5], 'vk_id': user[6], 'tg_id': user[7], 'access': user[8]}})

    else:
        return json.dumps({'success': False, 'description': 'Invalid user ID'})