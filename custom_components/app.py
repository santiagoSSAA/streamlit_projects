import streamlit as st
import streamlit.components.v1 as components

# Datos de los planes de precios
tiers = [
    {
        "name": "Hobby",
        "id": "tier-hobby",
        "href": "#",
        "priceMonthly": "$29",
        "description": "The perfect plan if you're just getting started with our product.",
        "features": [
            "25 products",
            "Up to 10,000 subscribers",
            "Advanced analytics",
            "24-hour support response time"
        ],
        "featured": False,
    },
    {
        "name": "Enterprise",
        "id": "tier-enterprise",
        "href": "#",
        "priceMonthly": "$99",
        "description": "Dedicated support and infrastructure for your company.",
        "features": [
            "Unlimited products",
            "Unlimited subscribers",
            "Advanced analytics",
            "Dedicated support representative",
            "Marketing automations",
            "Custom integrations"
        ],
        "featured": True,
    },
    {
        "name": "Enterprise",
        "id": "tier-enterprise",
        "href": "#",
        "priceMonthly": "$99",
        "description": "Dedicated support and infrastructure for your company.",
        "features": [
            "Unlimited products",
            "Unlimited subscribers",
            "Advanced analytics",
            "Dedicated support representative",
            "Marketing automations",
            "Custom integrations"
        ],
        "featured": True,
    },
    {
        "name": "Hobby",
        "id": "tier-hobby",
        "href": "#",
        "priceMonthly": "$29",
        "description": "The perfect plan if you're just getting started with our product.",
        "features": [
            "25 products",
            "Up to 10,000 subscribers",
            "Advanced analytics",
            "24-hour support response time"
        ],
        "featured": False,
    },
]

# Textos personalizados
title = "Pricing"
subtitle = "Choose the right plan for you"
description = "Choose an affordable plan that’s packed with the best features for engaging your audience, creating customer loyalty, and driving sales."

# Configuraciones de diseño
max_width = "1200px"
theme = "light"
cta_text = "Get started today"

# Declarar el componente
pricing_component = components.declare_component("pricing", url="http://localhost:3000")

# Usar el componente pasando todos los parámetros
pricing_component(
    tiers=tiers,
    title=title,
    subtitle=subtitle,
    description=description,
    maxWidth=max_width,
    theme=theme,
    ctaText=cta_text
)