import { Facebook, Instagram, Twitter, Mail, Phone, MapPin } from "lucide-react"

export function Footer() {
  return (
    <footer className="border-t border-border bg-card">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <div className="flex h-10 w-10 items-center justify-center rounded-full bg-primary">
                <span className="text-xl text-primary-foreground">🐾</span>
              </div>
              <span className="text-xl font-bold text-card-foreground">VetCare</span>
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Cuidado profesional y compasivo para tus mascotas desde 2010.
            </p>
            <div className="flex gap-4">
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Facebook className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Instagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Twitter className="h-5 w-5" />
              </a>
            </div>
          </div>

          <div>
            <h3 className="font-semibold text-card-foreground mb-4">Enlaces Rápidos</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a href="#inicio" className="text-muted-foreground hover:text-primary transition-colors">
                  Inicio
                </a>
              </li>
              <li>
                <a href="#servicios" className="text-muted-foreground hover:text-primary transition-colors">
                  Servicios
                </a>
              </li>
              <li>
                <a href="#equipo" className="text-muted-foreground hover:text-primary transition-colors">
                  Equipo
                </a>
              </li>
              <li>
                <a href="#citas" className="text-muted-foreground hover:text-primary transition-colors">
                  Agendar Cita
                </a>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold text-card-foreground mb-4">Servicios</h3>
            <ul className="space-y-2 text-sm">
              <li className="text-muted-foreground">Consultas Generales</li>
              <li className="text-muted-foreground">Vacunación</li>
              <li className="text-muted-foreground">Cirugía</li>
              <li className="text-muted-foreground">Emergencias 24/7</li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold text-card-foreground mb-4">Contacto</h3>
            <ul className="space-y-3 text-sm">
              <li className="flex items-start gap-2 text-muted-foreground">
                <MapPin className="h-4 w-4 mt-0.5 text-primary" />
                <span>Av. Principal 123</span>
              </li>
              <li className="flex items-center gap-2 text-muted-foreground">
                <Phone className="h-4 w-4 text-primary" />
                <span>+584124203030</span>
              </li>
              <li className="flex items-center gap-2 text-muted-foreground">
                <Mail className="h-4 w-4 text-primary" />
                <span>contacto@vetcare.com</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-border text-center text-sm text-muted-foreground">
          <p>&copy; {new Date().getFullYear()} VetCare. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  )
}
