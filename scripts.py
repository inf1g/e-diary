import random
from datacenter.models import Mark, Chastisement, Commendation, Lesson, Subject, Schoolkid


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3])
    marks.update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject):
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    school_subject = Subject.objects.filter(title=subject)
    lessons = Lesson.objects.filter(
        subject__in=school_subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date')
    commendation = random.choice(commendations)
    lesson = lessons.first()
    current_commendation = Commendation.objects.filter(created=lesson.date, schoolkid=schoolkid)
    if len(current_commendation) < 1:
        Commendation.objects.create(
            text=commendation,
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        return schoolkid
    except schoolkid.DoesNotExist:
        print(f"Ученик {schoolkid} не найден в базе данных")
    except schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников {schoolkid}")


def main():
    full_name = 'Фролов Иван Григорьевич'
    subject = "Музыка"
    schoolkid = get_schoolkid(full_name)
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject)


main()
