<!-- Formulario de Turnos: UX de 3 Clics -->
<div class="max-w-md mx-auto bg-white shadow-xl rounded-2xl p-8 font-sans border border-gray-100">
    <h2 class="text-3xl font-extrabold text-indigo-700 mb-6 text-center">Reserva tu Turno</h2>

    <!-- CLIC 1: Especialidad -->
    <div class="mb-8">
        <label class="block text-sm font-bold text-gray-600 uppercase tracking-wider mb-3">1. Elegí Especialidad</label>
        <select name="especialidad" 
                class="w-full p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-indigo-500 focus:ring-0 transition-all"
                hx-get="/buscar-medicos/" 
                hx-target="#seccion-medicos"
                hx-indicator="#loading">
            <option value="">Seleccionar...</option>
            <option value="clinica">Médico de Cabecera</option>
            <option value="pediatria">Pediatría</option>
            <option value="kinesiologia">Kinesiología</option>
        </select>
    </div>

    <!-- CLIC 2: Médico (Se carga solo) -->
    <div id="seccion-medicos" class="mb-8">
        <p class="text-gray-400 text-center italic py-4 border-2 border-dashed border-gray-100 rounded-xl">
            Acá aparecerán los profesionales disponibles
        </p>
    </div>

    <!-- CLIC 3: Confirmar -->
    <div id="paso-final" class="hidden">
        <button class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-black py-4 rounded-xl shadow-lg shadow-indigo-200 transform active:scale-95 transition-all text-lg">
            CONFIRMAR TURNO
        </button>
    </div>

    <!-- Feedback Visual -->
    <div id="loading" class="htmx-indicator flex justify-center mt-4">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-700"></div>
    </div>
</div>

<!-- Librerías de Estilo y Magia (HTMX) -->
<script src="https://unpkg.com/htmx.org@1.9.10"></script>
<script src="https://cdn.tailwindcss.com"></script>