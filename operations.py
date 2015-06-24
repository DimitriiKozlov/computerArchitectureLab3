__author__ = 'Dimitrii'
import couchdb

reserved_id = []

_couch = couchdb.Server("http://Di:pass@0.0.0.0:5984/")

if 'students' in _couch:
    _used_db = _couch['students']
    for student_id in _used_db:
        reserved_id.append(student_id)
else:
    _used_db = _couch.create('students')


def create(name, surname):
    doc = {'name': name, 'surname': surname}

    created_id, _ = _used_db.save(doc)
    reserved_id.append(created_id)
    return "New doc created"


def update(st_id, name, surname):
    if st_id < len(reserved_id):
        student_id = reserved_id[st_id]
    else:
        return "No such id"
    if student_id in _used_db:
        student = _used_db[student_id]
        student['surname'] = surname
        student['name'] = name
        print student
        _used_db[student_id] = student
    return "updated"


def read(st_id):
    if st_id < len(reserved_id):
        student_id = reserved_id[st_id]
    else:
        return "No such id"
    if student_id in _used_db:
        return str(_used_db[student_id])


def delete(st_id):
    if st_id < len(reserved_id):
        student_id = reserved_id[st_id]
    else:
        return "No such id"
    if student_id in _used_db:
        _used_db.delete(_used_db[student_id])
        reserved_id.remove(student_id)
    return "Deleted"


def read_all():
    lst = []
    for student_id in _used_db:
        lst.append(str(_used_db[student_id]))
    return lst
