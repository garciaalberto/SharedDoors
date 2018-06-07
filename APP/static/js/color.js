function changeColor(type) {
switch (type){
    case 'M':
        return 'green';
    case 'T':
        return 'orange';
    case 'P':
        return 'blue';
    case 'B':
        return 'purple';
    case 'R':
        return '#ff0040';
    default:
        return 'white';
    }
}