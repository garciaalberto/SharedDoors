from django import template

register = template.Library()


@register.simple_tag
def complete_task(event, points=100):
    users = event.users.all()
    event.is_completed = True
    for user in users:
        user.points_total += points
        user.points_monthly += points
        user.save()
    event.save()
