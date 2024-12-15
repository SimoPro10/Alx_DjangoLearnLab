from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def fetch_notifications(request):
    notifications = request.user.notifications.filter(read=False).order_by('-timestamp')
    response = [
        {
            'actor': notification.actor.username,
            'verb': notification.verb,
            'target': str(notification.target) if notification.target else None,
            'timestamp': notification.timestamp
        }
        for notification in notifications
    ]
    return JsonResponse({'notifications': response}, safe=False)

@login_required
def mark_notification_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notification.read = True
    notification.save()
    return JsonResponse({'message': 'Notification marked as read'}, status=200)

