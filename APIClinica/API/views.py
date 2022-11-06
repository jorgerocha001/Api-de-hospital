from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

from API.models import Medico, Consultas
from API.serializers import MedicoSerializer, ConsultasSerializer, CadastrarConsultasSerializer


class MedicoAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        medicos = Medico.objects.all()
        serializers = MedicoSerializer(medicos, many=True)
        return Response(serializers.data, status= HTTP_200_OK)

class CadastrarConsultasAPIView(APIView):
    def post(self, request, id, format=None):
        medicos = get_object_or_404(Medico, id=id)
        serializer = CadastrarConsultasSerializer(data=request.data)
        if serializer.is_valid():
            consulta = Consultas(
                nome_paciente= serializer.validated_data.get('nome'),
                medico= medicos
            )
            consulta.save()
            consluta_serializer= ConsultasSerializer(consulta, many=False)
            return Response(consluta_serializer.data, status= HTTP_201_CREATED)
        
        return Response({"message": "Houveram erros de validacao", "erros": serializer.errors}, status= HTTP_400_BAD_REQUEST)
