/**
 * Transforms an array of student objects into an array of their IDs.
 * @param {Array} listStudents - The array of student objects.
 * @returns {Array} An array of IDs, or an empty array if the input is invalid.
 */
export default function getListStudentIds(listStudents) {
  if (!Array.isArray(listStudents)) {
    return [];
  }

  return listStudents.map((student) => student.id);
}