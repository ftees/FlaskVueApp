<template>
  <div>
    <div v-if="training">
      <v-skeleton-loader :loading="training" type="card"></v-skeleton-loader>
    </div>

    <div v-else-if="trainingComplete">
      <p>Training complete!</p>
    </div>

    <div v-else>
      <button @click="$emit('train')">Train</button>
    </div>
  </div>
</template>

<script setup>
defineProps(['training', 'trainingComplete']);
</script>

<style scoped>
/* Styling specific to TrainingSection component */
</style>
