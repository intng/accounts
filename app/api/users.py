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
        return json.dumps(
            {'success': True,
             'user': {'id': id, 'name': name, 'surname': surname, 'schoolcard': schoolcard, 'approved': approved,
                      'form': form, 'vk_id': vk_id, 'tg_id': tg_id}})
