<template>
    <div class="w-max m-auto">
      <div class="grid w-max">
            <div class="text-center"><p>{{getPosition(player)}}</p></div>
            <div class="w-20 h-20 bg-cover" :class="team_path" :id="player.position"></div>
            <div class="text-cente grid grid-rows-2">
                <div v-if="player.status == 'i'" class="text-center bg-red-500 text-white px-1"><p>{{player.web_name}}</p></div>
                <div v-else-if="player.status == 'd'" class="text-center bg-orange-500 text-white px-1"><p>{{player.web_name}}</p></div>
                <div v-else class="text-center bg-black text-white px-1"><p>{{player.web_name}}</p></div>
                <div class="text-center bg-white"><p>{{ player.total_points }}</p></div>
          </div>
      </div>
  </div>
</template>

<script setup>
const props = defineProps({
  player: {
    type: Object,
    required: true,
  },
});
const {player} = props;
const team_path = "bg-[url('/assets/img/" + player.team + ".png')]"
function getPosition(player){
    if (player.element_type == 1){
        return "GKP"
    } else if(player.element_type == 2){
        return "DEF"
    } else if(player.element_type == 3){
        return "MID"
    }
    else{
        return "ATT"
    }
}
</script>