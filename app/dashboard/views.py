from django.shortcuts import render
from datetime import datetime, timedelta

def portal_analitico(request):
    # Datos simulados para la tabla
    datos = [
        {
            'fecha': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
            'cliente': 'Empresa Alpha',
            'metrica': 'Ventas',
            'valor': 125000
        },
        {
            'fecha': (datetime.now() - timedelta(days=4)).strftime('%Y-%m-%d'),
            'cliente': 'Empresa Beta',
            'metrica': 'Conversiones',
            'valor': 340
        },
        {
            'fecha': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
            'cliente': 'Empresa Gamma',
            'metrica': 'Tráfico Web',
            'valor': 15200
        },
        {
            'fecha': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
            'cliente': 'Empresa Alpha',
            'metrica': 'Retención',
            'valor': 87
        },
        {
            'fecha': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'cliente': 'Empresa Delta',
            'metrica': 'ROI',
            'valor': 245
        },
    ]
    
    context = {
        'datos': datos
    }
    
    return render(request, 'dashboard/portal.html', context)