import { Card, CardContent } from "@/components/ui/card"

const team = [
  {
    name: "Dra. María González",
    role: "Directora Médica",
    specialty: "Medicina Interna",
    image: "/female-veterinarian-professional.jpg",
  },
  {
    name: "Dr. Carlos Ramírez",
    role: "Cirujano Veterinario",
    specialty: "Cirugía General",
    image: "/male-veterinarian-surgeon.jpg",
  },
  {
    name: "Dra. Ana Martínez",
    role: "Especialista",
    specialty: "Dermatología",
    image: "/female-veterinarian-specialist.jpg",
  },
  {
    name: "Dr. Luis Torres",
    role: "Veterinario",
    specialty: "Emergencias",
    image: "/male-veterinarian-emergency.jpg",
  },
]

export function Team() {
  return (
    <section id="equipo" className="py-20 md:py-32">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center space-y-4 mb-16">
          <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl text-balance">
            Nuestro Equipo
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto text-pretty leading-relaxed">
            Profesionales certificados y apasionados por el cuidado animal
          </p>
        </div>

        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          {team.map((member, index) => (
            <Card key={index} className="border-border overflow-hidden hover:shadow-lg transition-shadow">
              <div className="aspect-square overflow-hidden bg-muted">
                <img
                  src={member.image || "/placeholder.svg"}
                  alt={member.name}
                  className="h-full w-full object-cover transition-transform hover:scale-105"
                />
              </div>
              <CardContent className="p-6 space-y-2">
                <h3 className="text-xl font-bold text-card-foreground">{member.name}</h3>
                <p className="text-sm font-medium text-primary">{member.role}</p>
                <p className="text-sm text-muted-foreground">{member.specialty}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
