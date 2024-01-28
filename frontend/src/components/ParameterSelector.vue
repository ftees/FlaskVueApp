<!-- src/components/ParameterSelector.vue -->
<template>
    <div>
      <label>Select Parameters:</label>
      <select v-model="selectedParameter">
        <option v-for="parameter in availableParameters" :key="parameter" :value="parameter">
          {{ parameter }}
        </option>
      </select>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  
  const props = defineProps(['selectedDataset', 'selectedModel']);
  
  const selectedParameter = ref(null);
  const availableParameters = ref([]);
  
  // Watch for changes in the selected dataset and model
  watch(() => [props.selectedDataset, props.selectedModel], ([dataset, model]) => {
    // Update available parameters based on the dataset and model
    updateParameters(dataset, model);
  });
  
  const updateParameters = (dataset, model) => {
    // Replace this with your actual logic to fetch or update parameters
    // The availableParameters should be an array of parameter names
    // Example: availableParameters.value = fetchParameters(dataset, model);
    availableParameters.value = ['param1', 'param2', 'param3']; // Placeholder
  };
  </script>
  
  <style scoped>
  /* Add your styling here if needed */
  </style>
  