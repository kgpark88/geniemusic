<template>
  <v-footer id="core-footer" fixed>
    <span class="font-weight-light copyright">
      &copy;
      {{ (new Date()).getFullYear() }}
      Danny, made with
      <!-- <v-icon color="tertiary" size="17">mdi-heart</v-icon> -->
      <v-icon color="pink" size="17">mdi-heart</v-icon>
      for a better ABC
    </span>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      links: [
        { name: 'Contact', Link: '/about' },
      ]
    })
  }
</script>

<style>
#core-footer {
  z-index: 0;
}
</style>
