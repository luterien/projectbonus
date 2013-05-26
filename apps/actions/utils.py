from django.contrib.contenttypes.models import ContentType

from apps.actions.models import Action, Invitation, Notification, Follow
from apps.profiles.models import Profile


def action(user, action_object, action_key, target_object=None, send_notification=True):
    """ 
        create a new action and send a notification to people following the target_object
    """
    action = Action.objects.new_action(user, action_object, action_key, target_object)

    if target_object and send_notification:
        notify_followers(action)


def invite(sender, cls, object_id, receiver=None, email=None):
    """
        if the receiver parameter is provided
        send an Invitation to the receiver

        otherwise send an email to the given address
    """
    if receiver:

        try:
            to = cls.objects.get(id=int(object_id))
            ivn = Invitation.objects.new(sender, to, receiver)
        except:
            to = None

        action(sender.user, receiver, "invite", target_object=to)
        
        # when an invitation is sent, notify the user
        #send_user_notification(action)

    if email:
        pass


def notify_followers(action, flws=None):
    """
        Create a notification from the given action,
        Send the message to everyone following the target_object of the action
    """
    sender = Profile.objects.get(user=action.user)

    # get followers for this object
    if not flws:
        flws = Follow.objects.filter(content_type=ContentType.objects.get_for_model(action.target_content_object.__class__),
                                     object_id=action.target_content_object.id)

    for flw in flws:

        follower = Profile.objects.get(user=flw.follower)

        if follower:
            notification = Notification(receiver=follower, sender=sender)
            notification._construct_notification_message(action)
            notification.save()


def start_following(user, follow_object):
    """
        Start following the target_object
        Currently, it is only activated when a user is assigned to a task, or creates a discussion
    """
    flw = Follow.objects.create_new(user, follow_object)

    return flw
