from rest_framework import routers
from globalis import views

app_name='globalis_app'

router = routers.DefaultRouter()
router.register(r'professor', views.ProfessorViewSet, basename='professor')
router.register(r'subject', views.SubjectViewSet, basename='subject')
router.register(r'textbook', views.TextBookViewSet, basename='textbook')

urlpatterns = router.urls