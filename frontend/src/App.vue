<!-- src/views/Home.vue -->
<template>
  <div class="main-container">
    <router-view></router-view>
  </div>
</template>

<script>
import UploadTrainingPage from '@/pages/UploadTrainingPage.vue';
import './main.css';

export default {
  components: {
    UploadTrainingPage,
  },
};
</script>

<style scoped>
/* Add your styling here if needed */
</style>
