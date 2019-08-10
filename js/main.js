document.addEventListener('DOMContentLoaded', () => {
   const usersTable = document.getElementById('users-table');

   selectHandle(usersTable);
});

function selectHandle(container) {
   const selectAllCb = container.querySelector('#select-all-cb');
   const allCheckbox = container.querySelectorAll('.users-table__checkbox');

   selectAllCb.addEventListener('click', event =>
      allCheckbox.forEach(item =>
         event.target.checked ?
         item.checked = true :
         item.checked = false
      ))
}