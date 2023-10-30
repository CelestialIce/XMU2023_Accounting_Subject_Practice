<template>
  <view>
    <text>首页</text>
    <view>
      <!-- 路由跳转练习，注意 open-type 的选择，另外，不要使用系统提示的相对路径! -->
      <navigator url="/pages/find/find" open-type="switchTab">
        <button type="default">跳转发现页面</button>
      </navigator>
      <navigator url="/subpages/chat/chat" open-type="redirect">
        <button type="default">跳转跟小姐姐聊天</button>
      </navigator>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {};
  }
};
</script>

<style>
/* 样式可以根据需要添加 */
</style>
