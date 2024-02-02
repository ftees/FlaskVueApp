<template>
  <v-app-bar :elevation="2" rounded>
    <template v-slot:prepend>
      <v-btn class="btn-logout" icon @click="logout">Logout </v-btn>
    </template>

    <v-app-bar-title></v-app-bar-title>
  </v-app-bar>
  <v-stepper
    v-model="currentStep"
    class="stepper"
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
import UploadFile from '@/components/UploadFile';
import ModelSelector from '@/components/ModelSelector';
import TrainingSection from '@/components/TrainingSection';
import { ref } from 'vue';

const currentStep = ref();

const logout = () => {
  fetch('http://localhost:5000/api/logout', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((res) => res.json())
    .then((data) => {
      if (data) {
        router.push('/login');
      } else {
        alert('Logout failed');
      }
    });
};
</script>
<style scoped>
.stepper {
  margin-top: 100px;
}

.btn-logout {
  margin-left: 50px;
}
</style>
