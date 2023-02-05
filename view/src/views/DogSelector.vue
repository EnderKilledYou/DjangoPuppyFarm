<script setup lang="ts">
import {defineComponent} from "vue";
import {imgs} from "@/views/img_api";

defineProps<{
  msg: string
}>()
defineComponent({
  setup() {

  },
  data() {
    return {imgs: imgs}
  }
})
</script>
<template>

  <div class="w-3/4 m-auto">

    <h2>dog-selector</h2>

    <!-- todo: Front end -->
  </div>


</template>

<style>

</style>
