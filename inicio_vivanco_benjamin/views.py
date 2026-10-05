from django.shortcuts import render

# Datos de prueba para enviar desde la vista hacia el template
TEMAS = [
    {
        'id': 1,
        'nombre': 'Videojuegos',
        'descripcion': 'Explora mundos virtuales épicos y setups de última generación con gráficos impresionantes.',
        'imagenes': ['images/videojuegos_1.jpg', 'images/videojuegos_2.jpg']
    },
    {
        'id': 2,
        'nombre': 'Tecnología',
        'descripcion': 'Descubre las tendencias del futuro, desde ciudades inteligentes hasta hardware avanzado.',
        'imagenes': ['images/tecnologia_1.jpg', 'images/tecnologia_2.jpg']
    }
]

def inicio(request):
    """
    Renderiza la vista principal con el listado de temas.
    El nombre del tema y la descripción se envían como data.
    """
    return render(request, 'inicio.html', {'temas': TEMAS})

def detalle_tema(request, tema_id):
    """
    Renderiza la vista de un tema específico con sus imágenes para el carrusel.
    """
    tema_seleccionado = next((t for t in TEMAS if t['id'] == tema_id), None)
    return render(request, 'tema.html', {'tema': tema_seleccionado})
