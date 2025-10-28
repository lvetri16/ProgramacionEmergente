"use client"

import type React from "react"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Calendar, Clock, User, Phone, Mail, PawPrint } from "lucide-react"
import { useState } from "react"

export function Appointments() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    petName: "",
    date: "",
    time: "",
    reason: "",
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log("[v0] Appointment form submitted:", formData)
    alert("¡Cita agendada exitosamente! Te contactaremos pronto.")
  }

  return (
    <section id="citas" className="py-20 md:py-32 bg-secondary/20">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid gap-12 lg:grid-cols-2 items-start">
          <div className="space-y-8">
            <div>
              <h2 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl text-balance mb-4">
                Agenda tu Cita
              </h2>
              <p className="text-lg text-muted-foreground text-pretty leading-relaxed">
                Completa el formulario y nos pondremos en contacto contigo para confirmar tu cita
              </p>
            </div>

            <div className="space-y-6">
              <div className="flex items-start gap-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                  <Clock className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <h3 className="font-semibold text-foreground mb-1">Horario de Atención</h3>
                  <p className="text-sm text-muted-foreground">Lunes a Viernes: 8:00 AM - 8:00 PM</p>
                  <p className="text-sm text-muted-foreground">Sábados: 9:00 AM - 6:00 PM</p>
                  <p className="text-sm text-muted-foreground">Domingos: 10:00 AM - 4:00 PM</p>
                </div>
              </div>

              <div className="flex items-start gap-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                  <Phone className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <h3 className="font-semibold text-foreground mb-1">Teléfono</h3>
                  <p className="text-sm text-muted-foreground">+58 212-555-6789</p>
                  <p className="text-sm text-muted-foreground">Emergencias: +58 414-555-4321</p>
                </div>
              </div>

              <div className="flex items-start gap-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10">
                  <Mail className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <h3 className="font-semibold text-foreground mb-1">Email</h3>
                  <p className="text-sm text-muted-foreground">contacto@vetcare.com.ve</p>
                </div>
              </div>
            </div>
          </div>

          <Card className="border-border">
            <CardHeader>
              <CardTitle className="text-card-foreground">Formulario de Cita</CardTitle>
              <CardDescription className="text-muted-foreground">
                Completa todos los campos para agendar tu cita
              </CardDescription>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="space-y-2">
                  <Label htmlFor="name" className="text-card-foreground">
                    <User className="inline h-4 w-4 mr-2" />
                    Tu Nombre
                  </Label>
                  <Input
                    id="name"
                    placeholder="Juan Pérez"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    required
                  />
                </div>

                <div className="grid gap-4 sm:grid-cols-2">
                  <div className="space-y-2">
                    <Label htmlFor="email" className="text-card-foreground">
                      <Mail className="inline h-4 w-4 mr-2" />
                      Email
                    </Label>
                    <Input
                      id="email"
                      type="email"
                      placeholder="juan@ejemplo.com"
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      required
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="phone" className="text-card-foreground">
                      <Phone className="inline h-4 w-4 mr-2" />
                      Teléfono
                    </Label>
                    <Input
                      id="phone"
                      type="tel"
                      placeholder="58 123-45678"
                      value={formData.phone}
                      onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                      required
                    />
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="petName" className="text-card-foreground">
                    <PawPrint className="inline h-4 w-4 mr-2" />
                    Nombre de tu Mascota
                  </Label>
                  <Input
                    id="petName"
                    placeholder="Max"
                    value={formData.petName}
                    onChange={(e) => setFormData({ ...formData, petName: e.target.value })}
                    required
                  />
                </div>

                <div className="grid gap-4 sm:grid-cols-2">
                  <div className="space-y-2">
                    <Label htmlFor="date" className="text-card-foreground">
                      <Calendar className="inline h-4 w-4 mr-2" />
                      Fecha
                    </Label>
                    <Input
                      id="date"
                      type="date"
                      value={formData.date}
                      onChange={(e) => setFormData({ ...formData, date: e.target.value })}
                      required
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="time" className="text-card-foreground">
                      <Clock className="inline h-4 w-4 mr-2" />
                      Hora
                    </Label>
                    <Input
                      id="time"
                      type="time"
                      value={formData.time}
                      onChange={(e) => setFormData({ ...formData, time: e.target.value })}
                      required
                    />
                  </div>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="reason" className="text-card-foreground">
                    Motivo de la Consulta
                  </Label>
                  <Textarea
                    id="reason"
                    placeholder="Describe brevemente el motivo de tu visita..."
                    value={formData.reason}
                    onChange={(e) => setFormData({ ...formData, reason: e.target.value })}
                    rows={4}
                    required
                  />
                </div>

                <Button type="submit" className="w-full bg-primary text-primary-foreground hover:bg-primary/90">
                  Agendar Cita
                </Button>
              </form>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  )
}
