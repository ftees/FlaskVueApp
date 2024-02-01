<template>
  <div>
    <div v-if="training">
      <v-skeleton-loader :loading="training" type="card"></v-skeleton-loader>
    </div>

    <div v-else-if="trainingComplete">
      <p>Token:</p>
      <span>{{ token }}</span>

    </div>

    <div v-else>
      <button @click="$emit('train')">Train</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['training', 'trainingComplete', 'token'],
};
</script>

<style scoped>
/* Styling specific to TrainingSection component */
</style>
