"use client"

import { Button } from "@/components/ui/button"
import { Menu, X } from "lucide-react"
import { useState } from "react"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-primary">
              <span className="text-xl text-primary-foreground">🐾</span>
            </div>
            <span className="text-xl font-bold text-foreground">VetCare</span>
          </div>

          <nav className="hidden md:flex items-center gap-6">
            <a href="#inicio" className="text-sm font-medium text-foreground hover:text-primary transition-colors">
              Inicio
            </a>
            <a href="#servicios" className="text-sm font-medium text-foreground hover:text-primary transition-colors">
              Servicios
            </a>
            <a href="#equipo" className="text-sm font-medium text-foreground hover:text-primary transition-colors">
              Equipo
            </a>
            <a href="#citas" className="text-sm font-medium text-foreground hover:text-primary transition-colors">
              Citas
            </a>
            <Button size="sm" className="bg-primary text-primary-foreground hover:bg-primary/90">
              Contacto
            </Button>
          </nav>

          <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)} aria-label="Toggle menu">
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {isMenuOpen && (
          <nav className="md:hidden py-4 space-y-4">
            <a
              href="#inicio"
              className="block text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Inicio
            </a>
            <a
              href="#servicios"
              className="block text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Servicios
            </a>
            <a
              href="#equipo"
              className="block text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Equipo
            </a>
            <a href="#citas" className="block text-sm font-medium text-foreground hover:text-primary transition-colors">
              Citas
            </a>
            <Button size="sm" className="w-full bg-primary text-primary-foreground hover:bg-primary/90">
              Contacto
            </Button>
          </nav>
        )}
      </div>
    </header>
  )
}
