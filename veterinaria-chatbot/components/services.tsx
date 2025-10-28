import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Stethoscope, Syringe, Scissors, Heart, Pill, Activity } from "lucide-react"

const services = [
  {
    icon: Stethoscope,
    title: "Consultas Generales",
    description: "Exámenes completos y diagnósticos precisos para mantener la salud de tu mascota.",
  },
  {
    icon: Syringe,
    title: "Vacunación",
    description: "Programas de vacunación personalizados para proteger a tu compañero.",
  },
  {
    icon: Scissors,
    title: "Cirugía",
    description: "Procedimientos quirúrgicos con tecnología avanzada y cuidado post-operatorio.",
  },
  {
    icon: Heart,
    title: "Emergencias",
    description: "Atención de urgencias disponible las 24 horas del día, todos los días.",
  },
  {
    icon: Pill,
    title: "Farmacia",
    description: "Medicamentos y suplementos de calidad para el tratamiento de tu mascota.",
  },
  {
    icon: Activity,
    title: "Laboratorio",
    description: "Análisis clínicos y estudios diagnósticos con resultados rápidos.",
  },
]

export function Services() {
  return (
    <section id="servicios" className="py-20 md:py-32 bg-secondary/20">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center space-y-4 mb-16">
          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl text-balance">
            Nuestros Servicios
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto text-pretty leading-relaxed">
            Ofrecemos una amplia gama de servicios veterinarios para cubrir todas las necesidades de tu mascota
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {services.map((service, index) => (
            <Card key={index} className="border-border hover:border-primary transition-colors">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10 mb-4">
                  <service.icon className="h-6 w-6 text-primary" />
                </div>
                <CardTitle className="text-card-foreground">{service.title}</CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-muted-foreground leading-relaxed">
                  {service.description}
                </CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
