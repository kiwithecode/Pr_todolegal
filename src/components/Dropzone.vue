<template>
    <div class="container">
        <div class="header">
            <h3>‹ Carga de Documentos</h3>
            <p>Sube tus documentos y ordènalos</p>
        </div>
        <!-- Dropzone para arrastrar y soltar archivos -->
        <div class="dropzone" @click="openFilePicker" @dragover.prevent="handleDragOver" @drop.prevent="handleDrop">
            <img v-if="selectedFiles.length === 0" src="../assets/subir.svg" alt="Upload Icon">
            <label v-if="selectedFiles.length === 0" for="filePicker" class="file-prompt">
                Arrastra tus archivos aquí o 
                <input type="file" id="filePicker" ref="fileInput" @change="handleFileChange" multiple style="display: none;">
                <span class="file-link">Buscar Archivo</span>
            </label>
            <!-- Lista de archivos subidos -->
            <ul class="file-list">
                <li v-for="(file, index) in selectedFiles" 
                    :key="index" 
                    draggable="true"
                    @dragstart="dragStart(index)"
                    @dragover="dragOver(index)"
                    @drop="drop(index)">
                {{ file.name }}
                <span @click="removeFile(index)"><img src="../assets/trs.svg" alt="Trash Icon"></span>
                </li>
            </ul>
        </div>
        <!-- Botón Siguiente -->
        <button @click="submitData">Siguiente</button>
        <!-- Modal para errores -->
        <div v-if="showModal" class="modal">
            Sólo se permiten archivos PDF.
            <button @click="closeModal">Cerrar</button>
        </div>
        <!-- Modal para éxitos -->
        <div v-if="showSuccessModal" class="modal">
            Subida exitosa.
            <button @click="closeSuccessModal">Cerrar</button>
        </div>
    </div>
</template>


<script lang="ts">
import { defineComponent, ref } from 'vue';
import { sendData } from '../service/servicio';

export default defineComponent({
  name: 'Dropzone',
  setup() {
    const selectedFiles = ref<File[]>([]);
    const showModal = ref(false);
    const showSuccessModal = ref(false);

    const handleFileChange = (event: Event) => {
      const uploadedFiles = (event.target as HTMLInputElement)?.files;
      if (uploadedFiles) {
        for (let i = 0; i < uploadedFiles.length; i++) {
          if (uploadedFiles[i].type !== "application/pdf") {
            showModal.value = true;
          } else {
            selectedFiles.value.push(uploadedFiles[i]);
          }
        }
      }
    };

    const handleDragOver = (event: DragEvent) => {
      event.preventDefault();
    };

    const handleDrop = (event: DragEvent) => {
      if (event.dataTransfer && event.dataTransfer.files) {
        for (let i = 0; i < event.dataTransfer.files.length; i++) {
          if (event.dataTransfer.files[i].type !== "application/pdf") {
            showModal.value = true;
          } else {
            selectedFiles.value.push(event.dataTransfer.files[i]);
          }
        }
      }
    };

    const removeFile = (index: number) => {
      selectedFiles.value.splice(index, 1);
    };

    const submitData = async () => {
      for (let file of selectedFiles.value) {
        try {
          const response = await sendData(file.name, file);
          console.log('Respuesta de la API:', response);
          showSuccessModal.value = true;
          selectedFiles.value = [];
        } catch (error) {
          console.error('Error al enviar el archivo:', error);
        }
      }
    };

    const closeModal = () => {
      showModal.value = false;
    };

    const closeSuccessModal = () => {
      showSuccessModal.value = false;
    };

    const openFilePicker = () => {
      const fileInput = (ref("fileInput") as any).value;
      if (fileInput) fileInput.click();
    };

    let draggedItemIndex: number | null = null;

    const dragStart = (index: number) => {
      draggedItemIndex = index;
    };

    const dragOver = (index: number) => {
      const draggedItem = selectedFiles.value[draggedItemIndex!];
      selectedFiles.value.splice(draggedItemIndex!, 1);
      selectedFiles.value.splice(index, 0, draggedItem);
      draggedItemIndex = index;
    };

    const drop = (_index: number) => {
      draggedItemIndex = null;
    };

    return {
      handleFileChange,
      handleDragOver,
      handleDrop,
      removeFile,
      submitData,
      closeModal,
      closeSuccessModal,
      openFilePicker,
      dragStart,
      dragOver,
      drop,
      showModal,
      showSuccessModal,
      selectedFiles
    };
  }
});
</script>


<style scoped src="src/components/css/Dropzone.css"></style>