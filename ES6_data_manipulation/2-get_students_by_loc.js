/**
 * Filters a list of students by a specific location.
 * @param {Array} students - The array of student objects.
 * @param {String} city - The city to filter by.
 * @returns {Array} An array of student objects located in the specified city.
 */
export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students.filter((student) => student.location === city);
}