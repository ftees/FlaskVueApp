<!-- src/views/Home.vue -->
<template>
  <div class="main-container">
    <v-app>
      <router-view></router-view>
    </v-app>
  </div>
</template>

<script>
import UploadTrainingPage from '@/pages/UploadTrainingPage.vue';
import './main.css';

export default {
  components: {
    UploadTrainingPage,
  },
  data: () => ({
    currentRoute: window.location.pathname,
  }),
  methods: {},
};
</script>

<style scoped></style>
