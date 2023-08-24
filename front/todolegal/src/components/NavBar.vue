<template>
  <nav class="navbar">
    <div class="logo">
      <img src="../assets/logo.svg" alt="Logo" />
    </div>
    <div class="right-section">
      <div class="secondary-logo">
        <img src="../assets/cont.svg" alt="Secondary Logo" />
      </div>
      <div class="drawer">
        <span>☰</span>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Navbar'
});
</script>

<style scoped src="src/components/css/NavBar.css"></style>
