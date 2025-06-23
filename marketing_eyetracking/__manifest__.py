# -*- coding: utf-8 -*-
{
    "name": "Eye-Tracking for Marketing & Research", # <-- CAMBIO: Nombre más completo
    "version": "16.0.1.0.0",
    "summary": "Analyze user attention with webcam eye-tracking to create heatmaps and optimize designs.",
    
    # La descripción ahora se tomará del index.html, pero es bueno dejar un resumen aquí.
    "description": """
        Integrates a webcam-based Eye-Tracking module into Odoo.
        This tool allows marketing teams and researchers to analyze user attention on websites, ads, and other digital content.
        It provides heatmaps, gaze plots, and session recordings, all processed locally in the browser to ensure user privacy.
    """,
    
    "author": "Eduardo Robles Russo",
    "website": "https://www.linkedin.com/in/eduardo-robles-russo-5133912b1/", # <-- AÑADIDO: Tu GitHub es un buen sitio web.
    "support": "eduroblesrusso82@gmail.com", # <-- AÑADIDO: Cambia esto por tu email.
    
    "category": "Marketing/Website", # <-- CAMBIO: Categoría más específica.
    "license": "LGPL-3", 
    
    "depends": ["base", "web"],
    
    "data": [
        "security/ir.model.access.csv",
        "views/analysis_views.xml",
        # Templates QWeb
        "static/src/xml/eye_tracking_component.xml",
        "static/src/xml/web_dialog_client_action.xml",
        "static/src/xml/chart-graphics/chart/chart_renderer.xml",
        "static/src/xml/chart-graphics/greet_dashboard.xml",
    ],
    
    "assets": {
        "web.assets_backend": [
            # Librerías
            "marketing_eyetracking/static/src/lib/bootstrap.bundle.min.js",
            "marketing_eyetracking/static/src/lib/d3.v3.min.js",
            "marketing_eyetracking/static/src/lib/localforage.js",
            "marketing_eyetracking/static/src/lib/webgazer.js",
            "marketing_eyetracking/static/src/lib/sweetalert.min.js",
            "marketing_eyetracking/static/src/lib/html2canvas.min.js",
            
            # JS de la aplicación
            "marketing_eyetracking/static/src/js/calibration.js",
            "marketing_eyetracking/static/src/js/main.js",
            "marketing_eyetracking/static/src/js/precision_store_points.js",
            "marketing_eyetracking/static/src/js/precision_calculation.js",
            "marketing_eyetracking/static/src/js/resize_canvas.js",
            "marketing_eyetracking/static/src/js/eye_tracking_component.js",
            "marketing_eyetracking/static/src/js/web_dialog_client_action.js",
            "marketing_eyetracking/static/src/js/google_analitics.js",
            "marketing_eyetracking/static/src/js/chart-graphics/chart/chart_renderer.js",
            "marketing_eyetracking/static/src/js/chart-graphics/greet_dashboard.js",
        ],
        # No se recomienda añadir Google Analytics en frontend para módulos de backend.
        # Si es para un sitio web, la clave correcta es 'website.assets_frontend'.
        # Si no, es mejor eliminarlo o gestionarlo de otra forma para evitar rechazos.
    },
    
    "images": [
        'static/description/main_screenshot.png',
        'static/description/icon.png'
    ],
    
    "price": 0.0,
    "currency": "EUR",
    
    "installable": True,
    "application": True,
}