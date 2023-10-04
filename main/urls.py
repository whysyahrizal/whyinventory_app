from django.urls import path
from main.views import show_main, show_item, create_item, show_json, show_xml, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_item_amount, delete_item, create_item, contact_us


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('show-item', show_item, name="show_item"),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('add/<int:id>', add_item_amount, name='add_item_amount'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('contact-us/', contact_us, name= 'contact_us'),
]