from django.shortcuts import render

def listadocoches(request):
    coches = [

        {"marca": "Toyota", "modelo": "Corolla", "cilindrada": "1.8", "precio": 22000,
         "foto": "peliculas/1.- Toyota.jpg"},
        {"marca": "Ford", "modelo": "Focus", "cilindrada": "1.5", "precio": 21000,
         "foto": "peliculas/2.- Ford.jpg"},
        {"marca": "BMW", "modelo": "Serie 3", "cilindrada": "2.0", "precio": 35000,
         "foto": "peliculas/3.- Bmw.jpg"},
        {"marca": "Audi", "modelo": "A4", "cilindrada": "2.0", "precio": 37000, "foto": "peliculas/4.audi.jpg"},
        {"marca": "Mercedes", "modelo": "Clase C", "cilindrada": "2.0", "precio": 39000,
         "foto": "peliculas/5. mercedes.jpg"},
    ]

    contexto = {
        'listado_coches': coches
    }

    return render(request, "gestion/carro.html", contexto)

