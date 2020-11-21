from Producer_Consumer.tasks.tasks import add
from rest_framework.response import Response
from rest_framework.decorators import api_view


class TestApi:

    @api_view(['GET'])
    def test(self):
        res = add.apply_async(args=(2, 3))
        ans = res.get()
        return Response({'ans': ans}, status=200)
