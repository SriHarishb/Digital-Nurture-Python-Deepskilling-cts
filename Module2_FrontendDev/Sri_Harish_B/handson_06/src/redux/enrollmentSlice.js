import { createSlice } from "@reduxjs/toolkit";

// Single source of truth for "which courses is the current student enrolled in".
const initialState = {
  enrolledCourses: [],
};

// createSlice bundles the reducer + auto-generated action creators together.
// Under the hood it uses Immer, so we can "mutate" `state` directly below
// (e.g. state.enrolledCourses.push) and it still produces an immutable update.
const enrollmentSlice = createSlice({
  name: "enrollment",
  initialState,
  reducers: {
    enroll(state, action) {
      const course = action.payload;
      // Prevent enrolling in the same course twice
      const exists = state.enrolledCourses.some((c) => c.id === course.id);
      if (!exists) {
        state.enrolledCourses.push(course);
      }
    },
    unenroll(state, action) {
      const courseId = action.payload;
      state.enrolledCourses = state.enrolledCourses.filter((c) => c.id !== courseId);
    },
  },
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;
