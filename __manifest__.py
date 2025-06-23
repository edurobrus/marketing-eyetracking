# -*- coding: utf-8 -*-
{
    "name": "Eye-Tracking for Marketing Campaigns",
    "version": "16.0.1.0.0", # <-- CAMBIO PRINCIPAL: Adaptado para Odoo 16.
    "summary": "Analyze marketing campaigns using webcam-based eye-tracking techniques.",
    "description": """
        This module allows recording and analyzing eye tracking data during marketing campaigns.
        Additionally, it integrates a webcam functionality to capture live video.
    """, # Se recomienda usar un archivo 'static/description/index.html' para una descripción más rica.
    
    "author": "Eduardo Robles Russo",
    "website": "https://www.linkedin.com/in/eduardo-robles-russo-5133912b1/", # AÑADIDO: Tu sitio web o el del producto.
    "support": "eduroblesrusso82@gmail.com", # AÑADIDO: Email de contacto para soporte.
    
    "category": "Marketing",
    "license": "LGPL-3", # AÑADIDO: ¡Esencial! La licencia es obligatoria.
    
    "depends": ["base", "web"],
    
    "data": [
        "security/ir.model.access.csv",
        "views/analysis_views.xml",
        # CAMBIO: Los templates XML/QWeb se declaran aquí, no en los assets.
        "static/src/xml/eye_tracking_component.xml",
        "static/src/xml/web_dialog_client_action.xml",
        "static/src/xml/chart-graphics/chart/chart_renderer.xml",
        "static/src/xml/chart-graphics/greet_dashboard.xml",
    ],
    
    "assets": {
        # CAMBIO: Los assets externos están prohibidos. Debes descargarlos e incluirlos localmente.
        "web.assets_frontend": [
            # Google Analytics - Debes descargar el script y guardarlo localmente.
            "marketing_eyetracking/static/src/lib/gtag.js", 
        ],
        "web.assets_backend": [
            # Librerías (libs)
            "marketing_eyetracking/static/src/lib/bootstrap.bundle.min.js",
            "marketing_eyetracking/static/src/lib/d3.v3.min.js",
            "marketing_eyetracking/static/src/lib/localforage.js",
            "marketing_eyetracking/static/src/lib/webgazer.js",
            "marketing_eyetracking/static/src/lib/sweetalert.min.js",
            "marketing_eyetracking/static/src/lib/html2canvas.min.js",
            
            # Archivos JavaScript de tu aplicación (organizados)
            "marketing_eyetracking/static/src/js/calibration.js",
            "marketing_eyetracking/static/src/js/main.js",
            "marketing_eyetracking/static/src/js/precision_store_points.js",
            "marketing_eyetracking/static/src/js/precision_calculation.js",
            "marketing_eyetracking/static/src/js/resize_canvas.js",
            "marketing_eyetracking/static/src/js/eye_tracking_component.js",
            "marketing_eyetracking/static/src/js/web_dialog_client_action.js",
            "marketing_eyetracking/static/src/js/chart-graphics/chart/chart_renderer.js",
            "marketing_eyetracking/static/src/js/chart-graphics/greet_dashboard.js",
        ],
    },
    
    "images": [
        'static/description/icon.png', # AÑADIDO: Icono del módulo (obligatorio)
    ],
    
    "price": 0.0, # AÑADIDO: Precio del módulo. Poner 0.0 si es gratuito.
    "currency": "EUR", # AÑADIDO: Moneda (EUR o USD).
    
    "installable": True,
    "application": True,
    "auto_install": False,
}