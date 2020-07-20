from library.models import Notification


def notifications(request):
    if request.user.is_anonymous == True:
        return {'notifications_count': 0}
    else:
        user = request.user
        notifications = Notification.objects.filter(user=user,
                                                    read=False)
        return {'notifications_count': notifications.count()}
