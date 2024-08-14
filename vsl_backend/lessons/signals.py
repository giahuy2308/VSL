from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Question, Choice, Content, Animation, Image, Lesson

from django.db.models import Q

def filter_instances(model, field_name=None, value=None):
    """
    Lọc danh sách các instance dựa trên giá trị của một trường cụ thể.
    :param model: Danh sách các instance của lớp Book
    :param field_name: Tên trường cần lọc (dưới dạng chuỗi)
    :param value: Giá trị cần so sánh
    :return: Danh sách các instance thỏa mãn điều kiện lọc
    """
    if not field_name == None:
        filtered_instances = [instance for instance in model if getattr(instance, field_name) == value]
        return filtered_instances
    return model.objects.all()

@receiver(post_save, sender=Question)
def create_or_update_choice(sender, instance, created, **kwargs):
    if created:
        Choice.objects.create(question=instance, title=instance.answer)
    else:    
        try:
            choice = Choice.objects.get(question=instance)
            choice.title = instance.answer
            choice.save(update_fields=["title"])
        except Choice.DoesNotExist:
            Choice.objects.create(question=instance, title=instance.answer)

@receiver(post_save, sender=Lesson)
def create_or_update_lesson(sender, instance, created, **kwargs):
    if created:
        if instance.no == 0:
            new_no = len(Lesson.objects.all()) + 1
            instance.no = new_no
            instance.save(update_fields=['no'])
        
    all_lessons = list(Lesson.objects.all())
    all_lessons.sort(key=lambda x: x.no)
    all_lessons.remove(instance)
    all_lessons.insert(instance.no - 1, instance)

    for i, lesson in enumerate(all_lessons, 1):
        if lesson.no != i :
            lesson.no = i 
            lesson.save(update_fields=['no'])

def update_no(instance, model, *sort_model):
    li = filter_instances(model, )


    for i, obj in enumerate(li, 1):
        if obj.no != i :
            obj.no = i 
            obj.save(update_fields=['no'])
    

def delete_section_content(instance):
    instance.section.content_quantity -= 1
    update_no(instance, False)
    instance.section.save(update_fields=["content_quantity"])

def create_or_update_section_content(instance, created):
    if created:
        instance.section.content_quantity += 1
    update_no(instance, True)
    instance.section.save(update_fields=["content_quantity"])

@receiver(post_save, sender=Content)
@receiver(post_save, sender=Image)
@receiver(post_save, sender=Animation)
def handle_content_image_animation(sender, instance, created, **kwargs):
    create_or_update_section_content(instance, created)


@receiver(post_delete, sender=Content)
@receiver(post_delete, sender=Image)
@receiver(post_delete, sender=Animation)
def handle_content_image_animation(sender, instance, **kwargs):
    delete_section_content(instance)


