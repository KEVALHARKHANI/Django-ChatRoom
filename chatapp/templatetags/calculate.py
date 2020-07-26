from django import template
from django.utils.safestring import mark_safe
register=template.Library()

@register.filter
def check(value1,*args,**kwargs):
    return str(value1)
@register.simple_tag
def other_msg(message,date,image):
    data="""<div class="d-flex justify-content-start mb-4">
								<div class="img_cont_msg">
									<img src="/Media/"""+image+""""" " class="rounded-circle user_img_msg">
								</div>
								<div class="msg_cotainer">"""+message+"""
									<span class="msg_time">"""+date+"""</span>
								</div>
							</div>
    """
    return mark_safe(data)

@register.simple_tag
def my_msg(message,date,image):
    data="""<div class="d-flex justify-content-end mb-4">
								<div class="msg_cotainer_send">"""+message+"""
									<span class="msg_time_send">"""+date+"""</span>
								</div>
								<div class="img_cont_msg">
									<img src="/Media/"""+image+""""" " class="rounded-circle user_img_msg">
								</div>
							</div>
    """
    return mark_safe(data)

@register.filter
def hash(dis,key):
    return dis[key];