from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        # from the example image in github, you can see a visualisation of what is happening here:
        return Response(serializer.data)

def post(self, request):
    # instead of saying 'all' like above, we create
    serializer = ProjectSerializer(data=request.data)
    # is valid?
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        # the above, is what we want our end point to do (excluding how to save a thing.)

# sometimes you may want to check to ensure the object is in the right 'Set' for instance if Ollie is te Fidofund and wants a particular pledge, software may say yes if pledge is one you created - no if you are not the owner(/user who created)
# as such, we have split the get from the response. The Get may become more complex, so. Split it out. 
class ProjectDetail(APIView):
    def get_object(self, pk):
        return Project.objects.get(pk=pk)
# object.get is a python thing, and expects an argument called pk. We are calling pk and assigning it pk (primary key)

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)