<template>
  <v-stepper v-model="currentStep" :items="['Step 1', 'Step 2', 'Step 3']"
    :next-text="currentStep === 2 ? 'Train' : 'Next'">
    <template v-slot:item.1>
      <v-card title="Dataset" flat>
        <UploadFile />
      </v-card>
    </template>

    <template v-slot:item.2>
      <v-card title="Modal" flat>
        <model-selector></model-selector>
      </v-card>
    </template>

    <template v-slot:item.3>
      <v-card flat>
        <training-section :training="true" :trainingComplete="false"></training-section>
      </v-card>
    </template>
  </v-stepper>
</template>

<script>
import UploadFile from "@/components/UploadFile.vue";
import ModelSelector from "@/components/ModelSelector.vue";
import TrainingSection from "@/components/TrainingSection.vue";

export default {
  components: {
    UploadFile,
    ModelSelector,
    TrainingSection,
  },
  data() {
    return {
      currentStep: 0,
    };
  },

};
</script>
