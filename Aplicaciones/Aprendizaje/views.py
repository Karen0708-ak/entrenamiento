from django.shortcuts import render
from sklearn.linear_model import LinearRegression
import numpy as np

def predecir_peso(request):
    resultado = None
    w0 = None
    w1 = None

    # Datos de entrenamiento
    edades = np.array([2, 3, 5, 7, 8]).reshape(-1, 1)
    pesos = np.array([14, 20, 32, 42, 44])

    # Crear y entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(edades, pesos)

    # Obtener coeficientes del modelo
    w0 = round(modelo.intercept_, 2)
    w1 = round(modelo.coef_[0], 2)

    if request.method == "POST":
        edad = float(request.POST.get("edad"))
        peso_predicho = modelo.predict([[edad]])[0]
        resultado = round(peso_predicho, 2)

    contexto = {
        "resultado": resultado,
        "w0": w0,
        "w1": w1,
    }

    return render(request, "aprend.html", contexto)

