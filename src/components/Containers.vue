<template>
    <div class="main-container">
        <!-- Primer contenedor -->
        <div class="action-container">
            <p>Firmar nuevo documento</p>
            <div class="step">
                <div class="circle">1</div>
                <p>Cargar documento</p>
            </div>
            <div class="step">
                <div class="circle">2</div>
                <p>Indicar firmantes</p>
            </div>
            <div class="step">
                <div class="circle">3</div>
                <p>Personalizaciones Opcionales</p>
            </div>
        </div>
    
        <!-- Espacio entre contenedores -->
        <div class="spacer"></div>
    
        <div class="bottom-containers">  <!-- Contenedor para los dos contenedores inferiores -->
            <!-- Segundo contenedor -->
            <div class="info-container">
                <h1>¿Cómo funciona?</h1>
                <img src="../assets/video.svg" alt="TodoLegal Image">
                <p>Este es un servicio gratuito de <span class="highlighted">todoLegal</span></p>
            </div>
            <!-- Tercer contenedor -->
            <div class="upload-container">
               <Dropzone/>
            </div>
        </div>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue';
import Dropzone from '../components/Dropzone.vue';

export default defineComponent({
  name: 'Docker',
  components: {
    Dropzone
  }
});
</script>

<style scoped src="src/components/css/Containers.css"></style>

