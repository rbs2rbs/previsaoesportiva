from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import sqlalchemy
import json
from credenciais import *

def dash(request):
    engine = sqlalchemy.create_engine(db_cred)
    result_PL = engine.execute('SELECT * FROM "Class_PL" ORDER BY c DESC , cl DESC, el DESC, p DESC, r DESC').fetchall()
    result_PD = engine.execute('SELECT * FROM "Class_PD" ORDER BY c DESC, cl DESC, el DESC, p DESC, r DESC').fetchall()
    result_SA = engine.execute('SELECT * FROM "Class_SA" ORDER BY c DESC, cl DESC, el DESC, p DESC, r DESC').fetchall()

    saida_PL = []
    for i in result_PL:
        saida_PL.append(
            {
                'time' : i[0],
                'c' : round(i[1]*100,2),
                'cl' : round(i[2]*100,2),
                'el' : round(i[3]*100,2),
                'p' : round(i[4]*100,2),
                'r' : round(i[5]*100,2)
            }
        )

    saida_PD = []
    for i in result_PD:
        saida_PD.append(
            {
                'time' : i[0],
                'c' : round(i[1]*100,2),
                'cl' : round(i[2]*100,2),
                'el' : round(i[3]*100,2),
                'p' : round(i[4]*100,2),
                'r' : round(i[5]*100,2)
            }
        )

    saida_SA = []
    for i in result_SA:
        saida_SA.append(
            {
                'time' : i[0],
                'c' : round(i[1]*100,2),
                'cl' : round(i[2]*100,2),
                'el' : round(i[3]*100,2),
                'p' : round(i[4]*100,2),
                'r' : round(i[5]*100,2)
            }
        )


    return render(request,"index.html",{'saida_PL' : saida_PL,'saida_PD' : saida_PD,'saida_SA' : saida_SA})
