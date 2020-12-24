from django.shortcuts import render

from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist

from like.models import LikeCount, LikeRecord
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)

def SuccessResponse(liked_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['liked_num'] = liked_num
    return JsonResponse(data)


def like_change(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(400, 'you should log in first')

    content_type = request.GET.get('content_type')
    object_id = int(request.GET.get('object_id'))

    try:
        content_type = ContentType.objects.get(model=content_type)
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(401, 'object not exist')

    if request.GET.get('is_like') == 'true':
        like_record, created = LikeRecord.objects.get_or_create(content_type=content_type,
                                                                object_id=object_id,
                                                                user=user)
        if created:
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type,
                                                                  object_id=object_id,
                                                                  )
            like_count.liked_num += 1
            like_count.save()
            return SuccessResponse(like_count.liked_num)
        else:
            return ErrorResponse(402, 'You can not like the same person twice')
    else:
        if LikeRecord.objects.filter(content_type=content_type,
                                     object_id=object_id,
                                     user=user).exists():
            like_record = LikeRecord.objects.get(content_type=content_type,
                                                 object_id=object_id,
                                                 user=user)
            like_record.delete()
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type,
                                                                  object_id=object_id,
                                                                  )
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return SuccessResponse(like_count.liked_num)
            else:
                return ErrorResponse(404, 'data error')
        else:

            return ErrorResponse(403, 'you can not cancel a like that not exits')