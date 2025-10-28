import { Button } from "@/components/ui/button"
import { Calendar, Clock, Heart } from "lucide-react"

export function Hero() {
  return (
    <section
      id="inicio"
      className="relative overflow-hidden bg-gradient-to-b from-secondary/30 to-background py-20 md:py-32"
    >
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid gap-12 lg:grid-cols-2 lg:gap-16 items-center">
          <div className="space-y-8">
            <div className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-4 py-2 text-sm font-medium text-primary">
              <Heart className="h-4 w-4" />
              Cuidado profesional desde 2010
            </div>

            <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl md:text-6xl lg:text-7xl text-balance">
              El mejor cuidado para tus mascotas
            </h1>

            <p className="text-lg text-muted-foreground md:text-xl text-pretty leading-relaxed">
              En VetCare brindamos atención veterinaria integral con tecnología de punta y un equipo de profesionales
              dedicados al bienestar de tu compañero.
            </p>

            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="bg-primary text-primary-foreground hover:bg-primary/90">
                <Calendar className="mr-2 h-5 w-5" />
                Agendar Cita
              </Button>
              <Button size="lg" variant="outline">
                <Clock className="mr-2 h-5 w-5" />
                Emergencias 24/7
              </Button>
            </div>

            <div className="grid grid-cols-3 gap-6 pt-8 border-t border-border">
              <div>
                <div className="text-3xl font-bold text-primary">15+</div>
                <div className="text-sm text-muted-foreground">Años de experiencia</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-primary">10K+</div>
                <div className="text-sm text-muted-foreground">Mascotas atendidas</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-primary">98%</div>
                <div className="text-sm text-muted-foreground">Satisfacción</div>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="aspect-square overflow-hidden rounded-3xl bg-muted">
              <img
                src="/happy-vet-dog-cat.png"
                alt="Veterinario con mascotas"
                className="h-full w-full object-cover"
              />
            </div>
            <div className="absolute -bottom-6 -left-6 rounded-2xl bg-card p-6 shadow-lg border border-border">
              <div className="flex items-center gap-4">
                <div className="flex h-12 w-12 items-center justify-center rounded-full bg-accent">
                  <Heart className="h-6 w-6 text-accent-foreground" />
                </div>
                <div>
                  <div className="text-sm font-medium text-card-foreground">Atención disponible</div>
                  <div className="text-2xl font-bold text-primary">24/7</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
