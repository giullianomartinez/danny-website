OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "DVJ Danny Website API",
        "version": "1.0.0",
        "description": (
            "API backend para contenido de landing, salud del servicio y "
            "solicitudes de contacto."
        ),
    },
    "servers": [{"url": "/"}],
    "tags": [
        {"name": "System", "description": "Estado del backend."},
        {"name": "Landing", "description": "Contenido publico de la landing."},
        {"name": "Contact", "description": "Recepcion de solicitudes de contacto."},
        {"name": "Reviews", "description": "Calificaciones publicas de clientes."},
    ],
    "paths": {
        "/api/health": {
            "get": {
                "tags": ["System"],
                "summary": "Revisar estado del backend",
                "responses": {
                    "200": {
                        "description": "Backend disponible.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/HealthResponse"}
                            }
                        },
                    }
                },
            }
        },
        "/api/landing": {
            "get": {
                "tags": ["Landing"],
                "summary": "Obtener contenido de la landing",
                "responses": {
                    "200": {
                        "description": "Contenido publico editable.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Landing"}
                            }
                        },
                    }
                },
            }
        },
        "/api/contact": {
            "post": {
                "tags": ["Contact"],
                "summary": "Crear solicitud de contacto",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ContactRequest"},
                            "example": {
                                "name": "Cliente Demo",
                                "contact": "+56 9 1234 5678",
                                "message": "Necesito DVJ para un matrimonio.",
                                "event_type": "Matrimonio",
                                "event_date": "2026-08-22",
                                "location": "Iquique",
                                "services": ["DVJ", "Resumen audiovisual"],
                            },
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Solicitud guardada y link de WhatsApp generado.",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/ContactResponse"
                                }
                            }
                        },
                    },
                    "400": {
                        "description": "Datos incompletos o invalidos.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ErrorResponse"}
                            }
                        },
                    },
                },
            }
        },
        "/api/reviews": {
            "get": {
                "tags": ["Reviews"],
                "summary": "Listar calificaciones",
                "responses": {
                    "200": {
                        "description": "Calificaciones publicadas.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ReviewList"}
                            }
                        },
                    }
                },
            },
            "post": {
                "tags": ["Reviews"],
                "summary": "Crear calificacion",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ReviewRequest"},
                            "example": {
                                "name": "Cliente Demo",
                                "rating": 5,
                                "comment": "Excelente musica y muy buena energia.",
                            },
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Calificacion guardada.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ReviewResponse"}
                            }
                        },
                    },
                    "400": {
                        "description": "Datos incompletos o invalidos.",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ErrorResponse"}
                            }
                        },
                    },
                },
            },
        },
        "/api/openapi.json": {
            "get": {
                "tags": ["System"],
                "summary": "Obtener especificacion OpenAPI",
                "responses": {
                    "200": {
                        "description": "Documento OpenAPI en formato JSON.",
                        "content": {"application/json": {"schema": {"type": "object"}}},
                    }
                },
            }
        },
    },
    "components": {
        "schemas": {
            "HealthResponse": {
                "type": "object",
                "required": ["status"],
                "properties": {"status": {"type": "string", "example": "ok"}},
            },
            "Landing": {
                "type": "object",
                "required": ["artist", "location", "tagline"],
                "properties": {
                    "artist": {"type": "string", "example": "DVJ Danny"},
                    "location": {"type": "string", "example": "Iquique, Chile"},
                    "tagline": {"type": "string"},
                    "summary": {"type": "string"},
                    "whatsapp_url": {"type": "string", "format": "uri"},
                    "stats": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Stat"},
                    },
                    "services": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Service"},
                    },
                    "packages": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Package"},
                    },
                    "timeline": {"type": "array", "items": {"type": "string"}},
                    "testimonials": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Testimonial"},
                    },
                },
            },
            "Stat": {
                "type": "object",
                "properties": {
                    "value": {"type": "string"},
                    "label": {"type": "string"},
                },
            },
            "Service": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "body": {"type": "string"},
                },
            },
            "Package": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "price": {"type": "string"},
                    "items": {"type": "array", "items": {"type": "string"}},
                },
            },
            "Testimonial": {
                "type": "object",
                "properties": {
                    "quote": {"type": "string"},
                    "author": {"type": "string"},
                },
            },
            "ContactRequest": {
                "type": "object",
                "required": ["name", "contact", "message"],
                "properties": {
                    "name": {"type": "string", "example": "Cliente Demo"},
                    "contact": {"type": "string", "example": "+56 9 1234 5678"},
                    "message": {
                        "type": "string",
                        "example": "Necesito DVJ para un matrimonio.",
                    },
                    "event_type": {"type": "string", "example": "Matrimonio"},
                    "event_date": {
                        "type": "string",
                        "format": "date",
                        "example": "2026-08-22",
                    },
                    "location": {"type": "string", "example": "Iquique"},
                    "services": {
                        "type": "array",
                        "items": {"type": "string"},
                        "example": ["DVJ", "Resumen audiovisual"],
                    },
                },
            },
            "ContactResponse": {
                "type": "object",
                "required": ["lead", "whatsapp_url"],
                "properties": {
                    "lead": {"$ref": "#/components/schemas/Lead"},
                    "whatsapp_url": {"type": "string", "format": "uri"},
                },
            },
            "ReviewRequest": {
                "type": "object",
                "required": ["name", "rating", "comment"],
                "properties": {
                    "name": {"type": "string", "example": "Cliente Demo"},
                    "rating": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 5,
                        "example": 5,
                    },
                    "comment": {
                        "type": "string",
                        "example": "Excelente musica y muy buena energia.",
                    },
                },
            },
            "ReviewResponse": {
                "type": "object",
                "required": ["review"],
                "properties": {"review": {"$ref": "#/components/schemas/Review"}},
            },
            "ReviewList": {
                "type": "object",
                "required": ["reviews"],
                "properties": {
                    "reviews": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Review"},
                    }
                },
            },
            "Review": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "rating": {"type": "integer", "minimum": 1, "maximum": 5},
                    "comment": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                },
            },
            "Lead": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "contact": {"type": "string"},
                    "event_type": {"type": "string"},
                    "event_date": {"type": "string"},
                    "location": {"type": "string"},
                    "services": {"type": "array", "items": {"type": "string"}},
                    "created_at": {"type": "string", "format": "date-time"},
                },
            },
            "ErrorResponse": {
                "type": "object",
                "required": ["error"],
                "properties": {"error": {"type": "string"}},
            },
        }
    },
}
