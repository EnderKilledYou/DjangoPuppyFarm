<script setup lang="ts">
import { ref } from "vue";
import { defineComponent } from 'vue';
import cocoSsd from "@tensorflow-models/coco-ssd";

import generated from "@tensorflow/tfjs-backend-webgl";

import generated0 from "@tensorflow/tfjs-backend-cpu";

const video = document.getElementById("video") as HTMLVideoElement;
defineComponent({
  name: 'App',
  setup(){
    const imgRef = ref("");
    const videoRef = ref<HTMLVideoElement>(video);
    const result = ref([]);
    async function detect() {
      const img = imgRef.value;
      const model = await cocoSsd.load();
      const predictions = await model.detect(img);
      result.value = predictions;
      console.log(predictions, img);
    }
    async function openCamera() {
      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({video: true}).then((stream)=>{
          videoRef.value.srcObject = stream;
        })
      }
    }

    return {
      imgRef,
      detect,
      result,
      videoRef,
      openCamera
    }
  }
});
</script>

<template>
  <main>
    <div class="w-3/4 m-auto">
      <div>
        <h1 class="text-2xl text-gray-800">Object detection with Tensorflow</h1>
        <div class="bg-gray-300 h-64 w-full rounded-lg shadow-md bg-cover bg-center">
          <img ref="imgRef"
               src="https://images.unsplash.com/photo-1503792501406-2c40da09e1e2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=752&q=80"
               alt="scissors" crossorigin="anonymous">
        </div>
      </div>
    </div>
  </main>
</template>
