from django.contrib import admin
from django.urls import path , include
from task.views import WorkerAPI , UnitAPI , VisitAPI
from task.views import units_list , make_a_visit
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Worker' , WorkerAPI)
router.register('Unit' , UnitAPI)
# router.register('Visit' , VisitAPI)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/admin/' , include(router.urls)),
    path('api/admin/Visits/' , VisitAPI.as_view()),
    path('api/units/' , units_list),
    path('api/make_visit/' , make_a_visit),
    path('api-auth/', include('rest_framework.urls')),
]
