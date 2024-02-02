<template>
  <v-stepper
    v-model="currentStep"
    :items="['Step 1', 'Step 2', 'Step 3']"
    :next-text="currentStep === 2 ? 'Train' : 'Next'"
  >
    <template v-slot:item.1>
      <v-card title="Dataset" flat>
        <UploadFile />
      </v-card>
    </template>

    <template v-slot:item.2>
      <v-card title="Model" flat>
        <ModelSelector />
      </v-card>
    </template>

    <template v-slot:item.3>
      <v-card flat>
        <TrainingSection :training="true" :trainingComplete="false" />
      </v-card>
    </template>
  </v-stepper>
</template>

<script setup>
import UploadFile from "@/components/UploadFile";
import ModelSelector from "@/components/ModelSelector";
import TrainingSection from "@/components/TrainingSection";
import { ref } from "vue";

const currentStep = ref();
</script>
