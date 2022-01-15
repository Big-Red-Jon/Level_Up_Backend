from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_gamer_profile(request):
    import pdb
    pdb.set_trace()
    return Response()
