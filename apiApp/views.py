from .serializers import PlanSerializer
from .models import Plan
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView

class PlanListView(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanCreateView(ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDeleteView(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_object(self):
        return Plan.objects.get(id=self.kwargs['id'])